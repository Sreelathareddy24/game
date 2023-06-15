document.addEventListener("DOMContentLoaded", function() {
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    var ballRadius = 10;
    var hitCount = parseInt("{{ hit_count }}");
    
    var padding = 30;
    var spacing = 2 * ballRadius + padding;
    var columns = Math.floor((canvas.width - padding * 2) / spacing);
    var rows = Math.ceil(hitCount / columns);

    var x = padding;
    var y = padding;
    for (var i = 0; i < hitCount; i++) {
        drawBall(x, y);
        
        x += spacing;
        if (x + ballRadius + padding >= canvas.width) {
            x = padding;
            y += spacing;
        }
    }

    function drawBall(x, y) {
        context.beginPath();
        context.arc(x, y, ballRadius, 0, Math.PI * 2);
        context.fillStyle = "#0095DD";
        context.fill();
        context.closePath();
    }
});
