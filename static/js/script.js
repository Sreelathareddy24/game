document.addEventListener("DOMContentLoaded", function() {
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    var ballRadius = 20;

    function drawBall(x, y) {
        context.beginPath();
        context.arc(x, y, ballRadius, 0, Math.PI*2);
        context.fillStyle = "#0095DD";
        context.fill();
        context.closePath();
    }

    // Draw a ball in the center of the canvas by default
    drawBall(canvas.width / 2, canvas.height / 2);

    canvas.addEventListener("click", function(event) {
        var rect = canvas.getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        drawBall(x, y);
        document.getElementById("hit").value = x;
    });
});
