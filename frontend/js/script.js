let chart;

async function predict() {
    try {
        let data = [
            getVal("age"),
            getVal("sex"),
            getVal("cp"),
            getVal("trestbps"),
            getVal("chol"),
            getVal("fbs"),
            getVal("restecg"),
            getVal("thalach"),
            getVal("exang"),
            getVal("oldpeak"),
            getVal("slope"),
            getVal("ca"),
            getVal("thal")
        ];

        if (data.includes(null)) {
            show("⚠️ Fill all fields!", "high-risk");
            return;
        }

        let res = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({features: data})
        });

        let result = await res.json();

        let risk = result.risk_percentage;
        let safe = 100 - risk;

        // Smarter result
        if (risk >= 70) {
            show(`⚠️ High Risk (${risk}%)`, "high-risk");
        } else if (risk >= 40) {
            show(`⚠️ Moderate Risk (${risk}%)`, "high-risk");
        } else {
            show(`✅ Safe (${risk}%)`, "safe");
        }

        showTip(risk);
        drawChart(risk, safe);

    } catch {
        show("❌ Server Error!", "high-risk");
    }
}

function getVal(id) {
    let v = document.getElementById(id).value;
    return v === "" ? null : Number(v);
}

function show(msg, cls) {
    let r = document.getElementById("result");
    r.innerText = msg;
    r.className = cls;
}

function showTip(risk) {
    let tip = document.getElementById("tip");

    if (risk >= 70) {
        tip.innerText = "⚠️ Consult a doctor immediately!";
    } else if (risk >= 40) {
        tip.innerText = "⚠️ Maintain healthy lifestyle.";
    } else {
        tip.innerText = "✅ You are healthy. Keep it up!";
    }
}

function drawChart(risk, safe) {
    let ctx = document.getElementById("riskChart");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Risk", "Safe"],
            datasets: [{
                data: [risk, safe],
                backgroundColor: ["#ef4444", "#22c55e"]
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: "top"
                }
            }
        }
    });
}