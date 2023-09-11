$(document).ready(function () {
  $("#address-form").on("submit", function (event) {
    $("#loading-post").show();
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      600
    );
    event.preventDefault();
    $.ajax({
      url: "address",
      type: "POST",
      data: $(this).serialize(),
      dataType: "json",
      success: function (response) {
        console.log(response.success);
        if (response.success) {
          $("#address-form").trigger("reset");
          $("#loading-post").hide();
          $("#alert-success").show();
          $("#message-alert-success").text("Konfigurasi anda berhasil !");
        } else {
          $("#loading-post").hide();
          $("#address-form").trigger("reset");
          $("#alert-failed").show();
          $("#message-alert-failed").text("Konfigurasi anda gagal !");
        }
      },
    });
  });
  $("#icon-close-success").on("click", () => {
    $("#alert-success").hide();
  });
  $("#icon-close-failed").on("click", () => {
    $("#alert-failed").hide();
  });
});
