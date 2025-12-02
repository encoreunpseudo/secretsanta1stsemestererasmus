// Secret Santa assignments encrypted in Base64.
// Key = name of the person giving
// Value = Base64(name of the person receiving)
// Each person gives to exactly one other person, and everyone receives a gift.

const assignments = {
    "Amel": "RnJhbno=",       // Base64 encoded
    "Mayline": "RWxpYXM=",
    "Lara": "QW1lbA==",
    "Franz": "QW1lbGlh",
    "Amelia": "TWF5bGluZQ==",
    "Elvis": "TGFyYQ==",
    "Elias": "RWx2aXM="
  };
  
  // Prevent someone from looking at multiple names
  // by saving their choice in the browser.
  const STORAGE_KEY = "secret_santa_name";

  function decodeBase64(b64) {
    // atob = standard JS function to decode Base64
    return atob(b64);
  }

  window.addEventListener("DOMContentLoaded", () => {
    const select = document.getElementById("name");
    const btn = document.getElementById("revealBtn");
    const result = document.getElementById("result");

    // If the person already chose their name, retrieve it
    const savedName = localStorage.getItem(STORAGE_KEY);
    if (savedName && assignments[savedName]) {
      select.value = savedName;
    }

    btn.addEventListener("click", () => {
      const nameKey = select.value;

      if (!nameKey) {
        result.textContent = "Please first choose your name from the list.";
        return;
      }

      const encoded = assignments[nameKey];
      if (!encoded) {
        result.textContent = "No assignment found (talk to the organizer 😅).";
        return;
      }

      const recipient = decodeBase64(encoded);

      result.textContent = `You need to give a gift to: ${recipient} 🎄`;

      // Save the name to prevent "playing" with others
      localStorage.setItem(STORAGE_KEY, nameKey);
    });
  });
  