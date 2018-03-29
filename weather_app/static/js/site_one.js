// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('myImg');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}


// $(document).ready(function() {

    // $.getJSON("https://graph.facebook.com/1471936623033617/feed?access_token=780986788681337|ad36e56c035e56f9f1dc1a57946143f4", function() {})

    //     .done(function(data) {
    //         console.log(data);
    //         $.each(data.data.slice(0, 3), function(i, item) {
    //             created_date = new Date(item.created_time);
    //             title = item.story || "TamilnaduWeatherMan";
    //             $('#fb_post').append('<div><h4>' + title + ' </h4> <small>' + created_date + '</small><br><br><span style="white-space: pre-line">' + item.message + '</span></div><br>')
    //         })
    //     })

    //     .fail(function() {
    //         console.log("Error to get FB post");
    //         alert("oops!!! There were some errors :(")
    // });
// });