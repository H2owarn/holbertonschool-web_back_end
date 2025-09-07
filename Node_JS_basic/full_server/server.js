const express = require('express');
const routes = require('./routes/index');

const app = express();
const PORT = 1245;

// Use the imported routes
app.use('/', routes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

module.exports = app;