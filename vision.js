const cv = require('opencv');

// Load an image
cv.readImage('speedometer.jpg', function(err, img) {
    if (err) {
        console.error(err);
        return;
    }

    // Convert the image to grayscale
    cv.cvtColor(img, img, cv.COLOR_BGR2GRAY);

    // Detect the speedometer
    let speedometerX = 0;  // Adjust this to match the actual location of the speedometer
    let speedometerY = 0;  // Adjust this to match the actual location of the speedometer
    let speedometerWidth = 100;  // Adjust this to match the actual width of the speedometer
    let speedometerHeight = 100;  // Adjust this to match the actual height of the speedometer
    let speedometerThreshold = 128;  // Adjust this to match the actual threshold for detecting the speedometer

    let count = 0;
    for (let y = speedometerY; y < speedometerY + speedometerHeight; y++) {
        for (let x = speedometerX; x < speedometerX + speedometerWidth; x++) {
            let grayValue = img.getAt(x, y)[0];
            if (grayValue > speedometerThreshold) {
                count++;
            }
        }
    }

    console.log("Count: " + count);
});
