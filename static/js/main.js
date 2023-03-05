
const maxNumberOfChoices = 5

const availableChoices = new Map();
availableChoices.set("subway", "Метро");
availableChoices.set("polyclinic", "Поликлиника");
availableChoices.set("fitness", "Фитнес зал");
availableChoices.set("school", "Школа");
availableChoices.set("kindergarten", "Детский сад");

const unavailbaleChoices = new Map();

function toggleAddElemBtn(){
    $("#addElemBtn").toggleClass('d-none');
}

function drawChoiceButtons(){
    let listChoicesButtons = document.getElementById("listVariantsToAdd");
    availableChoices.forEach(function (name, value) {
        let button = document.createElement("button")
        button.type = "button"
        button.value = value
        button.textContent = name
        button.setAttribute( "onClick", "javascript: addElementToList(this.value);" );
        button.setAttribute( "class", "list-group-item list-group-item-action choiceButton");
        console.log(button)
        listChoicesButtons.appendChild(button)
    })
    $("#addElemBtn").toggleClass('d-none');
}

function removeChoiceButtons(){
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


function addElementToList(choice){

    let blockElement = document.createElement("div");

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

function removeListElement(removeButton){
    makeChoiceAvailable(removeButton.value)
    removeButton.parentElement.parentElement.remove()
}
