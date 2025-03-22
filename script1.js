async function getTrafficData() {
    const query = `{
        trafficStatus(id: 1) {
            location
            congestionLevel
        }
    }`;

    const response = await fetch("http://localhost:5000/graphql", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await response.json();
    document.getElementById("result").innerText = 
        `Location: ${data.data.trafficStatus.location}, Congestion: ${data.data.trafficStatus.congestionLevel}`;
}
