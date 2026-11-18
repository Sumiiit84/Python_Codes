
const express = require('express');

const app = express();

app.get('/about', (req, res) => {
    res.json({
        project: "Student API",
        version: "1.0",
        created_by: "Sumeet Dongare"
    });
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
