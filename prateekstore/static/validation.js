function valid() {
    var name = document.getElementById("Name").value;
    var email = document.getElementById("Email").value;
    var mobileNumber = document.getElementById("MobileNumber").value;
    var password = document.getElementById("Password").value;
    var cpassword = document.getElementById("CPassword").value;
  
    // Validate name field
    if (name == "") {
      alert("Please enter your name");
      return false;
    }
  
    // Validate email field
    if (email == "") {
      alert("Please enter your email");
      return false;
    } else {
      var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        alert("Please enter a valid email");
        return false;
      }
    }
  
    // Validate mobile number field
    if (mobileNumber == "") {
      alert("Please enter your mobile number");
      return false;
    } else {
      var mobileNumberPattern = /^\d{11}$/;
      if (!mobileNumberPattern.test(mobileNumber)) {
        alert("Please enter a valid 10 digit mobile number");
        return false;
      }
    }
  
    // Validate password field
    if (password == "") {
      alert("Please enter a password");
      return false;
    } else {
      var passwordPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
      if (!passwordPattern.test(password)) {
        alert("Please enter a password of at least 8 characters with at least one lowercase letter, one uppercase letter, and one number");
        return false;
      }
    }
  
    // Validate confirm password field
    if (cpassword == "") {
      alert("Please confirm your password");
      return false;
    } else {
      if (cpassword != password) {
        alert("Passwords do not match");
        return false;
      }
    }
  
    // If all fields are valid, allow form submission
    return true;
  }
  