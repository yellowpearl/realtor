const maxNumberOfChoices = 5

const availableChoices = new Map();
availableChoices.set("subway", "Метро");
availableChoices.set("grocery", "Продуктовый магазин");
availableChoices.set("polyclinic", "Поликлиника");
availableChoices.set("fitness", "Фитнес зал");
availableChoices.set("school", "Школа");
availableChoices.set("kindergarten", "Детский сад");
availableChoices.set("moscow_centre", "Центр города");
availableChoices.set("mall", "Торговый центр");
availableChoices.set("bar", "Бар");


const unavailbaleChoices = new Map();

function drawChoiceButtons() {
    let listChoicesButtons = document.getElementById("listVariantsToAdd");
    availableChoices.forEach(function (name, value) {
        let button = document.createElement("button")
        button.type = "button"
        button.value = value
        button.textContent = name
        button.setAttribute("onClick", "javascript: addElementToList(this.value);");
        button.setAttribute("class", "list-group-item list-group-item-action choiceButton");
        listChoicesButtons.appendChild(button)
    })
    $("#addElemBtn").toggleClass('d-none');
}

function removeChoiceButtons() {
    const buttons = document.querySelectorAll('.choiceButton');
    buttons.forEach(button => {
        button.remove();
    });
    $("#addElemBtn").toggleClass('d-none');
}

function getCopyElement(elementId) {
    let node = document.getElementById(elementId);
    let copyElem = node.cloneNode(true)
    copyElem.removeAttribute('id');
    return copyElem
}

function getHeaderElement(elementName) {
    let block = getCopyElement("elementHeader")
    let blockTitle = getCopyElement("blockTitle")
    blockTitle.textContent = availableChoices.get(elementName)
    let blockExcBnt = getCopyElement("blockExcBnt")
    blockExcBnt.value = elementName
    block.appendChild(blockTitle)
    block.appendChild(blockExcBnt)
    return block
}


function addElementToList(choice) {

    let blockElement = document.createElement("div");
    blockElement.classList.add('choice');
    let header = getHeaderElement(choice)
    let selectTransportType = getCopyElement("selectTransportType");
    let selectTravelTime = getCopyElement("selectTravelTime");
    let hrLine = document.createElement('hr');

    blockElement.appendChild(header);
    blockElement.appendChild(selectTransportType);
    blockElement.appendChild(selectTravelTime);
    blockElement.appendChild(hrLine);

    let formElementsList = document.getElementById("formElementsList");
    formElementsList.appendChild(blockElement);
    removeChoiceButtons()
    makeChoiceUnavailable(choice)
    activateOpenModalButton()
}

function makeChoiceUnavailable(choiceName) {
    let choice = availableChoices.get(choiceName)
    unavailbaleChoices.set(choiceName, choice)
    availableChoices.delete(choiceName)

    if (availableChoices.size === 0) {
        $("#addElemBtn").addClass('d-none');
    }
    if (unavailbaleChoices.size === maxNumberOfChoices) {
        $("#addElemBtn").addClass('d-none');
    }
}

function makeChoiceAvailable(choiceName) {
    let choice = unavailbaleChoices.get(choiceName)
    availableChoices.set(choiceName, choice)
    unavailbaleChoices.delete(choiceName)

    if (availableChoices.size === 1) {
        $("#addElemBtn").removeClass('d-none');
    }
    if (unavailbaleChoices.size < maxNumberOfChoices) {
        $("#addElemBtn").removeClass('d-none');
    }

}

function removeListElement(removeButton) {
    makeChoiceAvailable(removeButton.value)
    removeButton.parentElement.parentElement.remove()
    if (unavailbaleChoices.size === 0) {
        deactivateOpenModalButton()
    }
}


function sendSelectedChoices(isPaid) {
    const choicesElements = document.querySelectorAll('.choice');
    let choices = []
    choicesElements.forEach(choice => {
        let choiceMap = {
            place: choice.getElementsByClassName("removeChoiceButton")[0].value,
            transport: choice.getElementsByClassName("selectTransportType")[0].value,
            travel_time: choice.getElementsByClassName("selectTravelTimeSelect")[0].value
        }
        choices.push(choiceMap)
    });
    let data = {
        choices: choices,
        email: document.getElementById("defaultForm-email1").value,
        is_paid: isPaid
    }
    makeAjaxWithChoices(data)
}

function makeAjaxWithChoices(data) {
    $.ajax({
        type: 'post',
        url: '/api/v1/create_map',
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function (rData) {
            if (data.is_paid) {
                window.location.replace("success_send_choices_paid.html");
            } else {
                window.location.replace("success_send_choices.html");
            }
        },
        error: function (jqXHR, exception) {
            console.log("ERR")
            //window.location.replace("error_send_choices.html");
        }
    });
}

function activateOpenModalButton() {
    document.getElementById("openModalButton").disabled = false;
}

function deactivateOpenModalButton() {
    document.getElementById("openModalButton").disabled = true;
}


function validateEmail(is_paid) {
    let email = document.getElementById("defaultForm-email1").value
    if (emailIsValid(email)) {
        if (is_paid) {
            $('#sendSelectedChoiceBtnIsPaid').click();
        } else {
            $('#sendSelectedChoiceBtnIsNotPaid').click();
        }
    } else {
        $('#defaultForm-email1').addClass('is-invalid')
        $('#invalidEmailDesc').removeClass('d-none')
    }
}

function emailIsValid(email) {
  let regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}