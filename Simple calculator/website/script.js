function calculate() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const op = document.getElementById("operation").value;
    let result;

    if(op === "add") result = num1 + num2;
    else if(op === "subtract") result = num1 - num2;
    else if(op === "multiply") result = num1 * num2;
    else if(op === "divide") result = num2 !== 0 ? num1 / num2 : "Cannot divide by zero";

    document.getElementById("result").innerText = "Result: " + result;
}
