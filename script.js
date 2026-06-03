function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    if(user === "" || pass === ""){
        alert("Please enter credentials");
        return;
    }

    // Dummy login (backend later)
    window.location.href = "dashboard.html";
}

function analyzeText() {

    let text = document.getElementById("userInput").value;

    if (text.trim() === "") {
        alert("Please describe your situation.");
        return;
    }

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById("category").innerText =
        "Predicted Category: " + data.category;

    document.getElementById("advice").innerHTML =
        "<b>Applicable Law:</b> " + data.law + "<br>" +
        "<b>Relevant Section:</b> " + data.section + "<br>" +
        "<b>Guidance:</b> " + data.advice;

    document.getElementById("resultBox").style.display = "block";
})
    .catch(error => {
        console.error("Error:", error);
        alert("Backend not connected.");
    });
}