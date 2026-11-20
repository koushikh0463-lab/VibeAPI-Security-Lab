const output = document.getElementById("response-output");
const urlLabel = document.getElementById("response-url");
const statusLabel = document.getElementById("response-status");
const timeLabel = document.getElementById("response-time");

document.querySelectorAll(".endpoint").forEach((button) => {
  button.addEventListener("click", async () => {
    const path = button.dataset.url;
    urlLabel.textContent = path;
    output.textContent = "Loading response...";
    statusLabel.textContent = "SENDING";
    const started = performance.now();
    try {
      const response = await fetch(path);
      const body = await response.text();
      let formatted = body;
      try { formatted = JSON.stringify(JSON.parse(body), null, 2); } catch (_) {}
      output.textContent = formatted;
      statusLabel.textContent = `${response.status} ${response.statusText || ""}`.trim();
      timeLabel.textContent = `${Math.round(performance.now() - started)} ms`;
    } catch (error) {
      output.textContent = `Request failed: ${error.message}`;
      statusLabel.textContent = "ERROR";
      timeLabel.textContent = "Request failed";
    }
  });
});
