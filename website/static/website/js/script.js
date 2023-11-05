{/* <script> */}
  document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Assuming a successful form submission
    // You would typically use AJAX to send the form data to the server
    // and get a response back to determine success or failure

    // Simulate a successful submission
    const isSuccessful = true;

    if (isSuccessful) {
      alert("Form submitted successfully!"); // Display a simple alert
      // You can replace this alert with a more user-friendly notification
    } else {
      alert("Form submission failed. Please try again.");
    }
  });
// </script>