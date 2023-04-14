// arrow key event listener
document.addEventListener('keydown', function(event) {
    const speed = 0.1;
    switch (event.key) {
        case "ArrowLeft":
            camera.position.x -= speed;
            break;
        case "ArrowRight":
            camera.position.x += speed;
            break;
        case "ArrowUp":
            camera.position.y += speed;
            break;
        case "ArrowDown":
            camera.position.y -= speed;
            break;
    }
    controls.update();
});

// mouse wheel zoom control
function onDocumentMouseWheel(event) {
    const zoomAmount = event.deltaY * 0.05;
    const minZoom = 1;
    const maxZoom = 200;
    camera.position.z = Math.min(maxZoom, Math.max(minZoom, camera.position.z - zoomAmount));
}
document.addEventListener('wheel', onDocumentMouseWheel, false);