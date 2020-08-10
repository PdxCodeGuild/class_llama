let codex = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"};
let code_numbers = [];
let new_code_numbers = [];
let new_phrase_list = [];
let phrase = prompt("enter a phrase to send to your spy: ").toLowerCase();
let offset = parseInt(prompt("enter a number with which to encode your message: "));
let new_phrase = ""

let phrase_list = phrase.split("");

function numberize(letter) {
    if (letter === " ") {
        return " "
    } else {
        for (number in codex) {
            if (codex[number] == letter) {
                return number
            };
        };
    };

};

function encode(number) {
    if (number == " ") {
        return " ";
    } else {
    return parseInt(number) + offset
    };
};

function letterize(character) {
    if (character == " ") {
        return " "
    } else if (character > 26) {
        character = character -26;
        for (number in codex) {
            if (character == number) {
                return codex[character]
            }
        };
    } else {
        for (number in codex) {
            if (character == number) {
                return codex[character]
            };
        };
    };
};



code_numbers = phrase_list.map(numberize);
new_code_numbers = code_numbers.map(encode);
new_phrase_list = new_code_numbers.map(letterize);
new_phrase = new_phrase_list.join("");



alert(new_phrase)