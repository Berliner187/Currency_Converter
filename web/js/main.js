document.getElementById("rDollar").onclick = async function display_Dollar() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_Dollar()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out + " ₽";
};

document.getElementById("rEuro").onclick = async function display_Euro() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_Euro()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out + " ₽";
};

document.getElementById("rPound").onclick = async function display_Pound() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_Pound()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out + " ₽";
};

document.getElementById("rHryvnia").onclick = async function display_Hryvnia() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_Hryvnia()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out + " ₽";
};

document.getElementById("rYuan").onclick = async function display_Yuan() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_Yuan()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out + " ₽";
};

document.getElementById("rArmenianDram").onclick = async function display_ArmenianDram() {
    let userNum = document.getElementById("rNumber").value;
    let num = await eel.check_ArmenianDram()();
    let out = userNum * num

    document.getElementById("info_ruble").innerHTML = out  + " ₽";
};



document.getElementById("cDollar").onclick = async function display_Dollar() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_Dollar()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out + " $";
};

document.getElementById("cEuro").onclick = async function display_Euro() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_Euro()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out + " €";
};

document.getElementById("cPound").onclick = async function display_Pound() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_Pound()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out + " £";
};

document.getElementById("cHryvnia").onclick = async function display_Hryvnia() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_Hryvnia()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out + " ₴";
};

document.getElementById("cYuan").onclick = async function display_Yuan() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_Yuan()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out + " ¥";
};

document.getElementById("cArmenianDram").onclick = async function display_ArmenianDram() {
    let userNum = document.getElementById("cNumber").value;
    let num = await eel.check_ArmenianDram()();
    let out = userNum / num

    document.getElementById("info_currency").innerHTML = out  + " ֏";
};