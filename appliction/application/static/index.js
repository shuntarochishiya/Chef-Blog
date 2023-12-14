
$(document).ready(function () {
    // Toggle password visibility
    $(".eye").on("click", function () {
        var passwordInput = $(".password-input");
        var eyeIcon = $(".eye");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            eyeIcon.html('<i class="fa-solid fa-eye-slash"></i>');
        } else {
            passwordInput.attr("type", "password");
            eyeIcon.html('<i class="fa-solid fa-eye"></i>');
        }
    });
});
