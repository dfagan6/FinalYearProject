// create a new Three.js scene
const scene = new THREE.Scene();

// create a new Three.js camera and position it
const camera = new THREE.PerspectiveCamera(25, window.innerWidth / (2*window.innerHeight), 0.1, 2000);
camera.position.x = 7;
camera.position.y = 8;
camera.position.z = 50;

// create a new Three.js renderer and add it to the document
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


// load the image data from the JSON file
fetch('imageLocations.JSON')
	.then(response => response.json())
	.then(data => {
		// iterate over each image file in the JSON data
		for (const [fileName, position] of Object.entries(data)) {
			// create a new Three.js texture from the image file
			const texture = new THREE.TextureLoader().load("Images_100x100\\"+fileName);
			// create a new Three.js material using the texture
			const material = new THREE.MeshBasicMaterial({ map: texture });
			// create a new Three.js mesh using a plane geometry and the material
			const geometry = new THREE.PlaneGeometry(0.1,0.1);
			const mesh = new THREE.Mesh(geometry, material);
			// set the position of the mesh based on the coordinates in the JSON data
			mesh.position.x = position[0];
			mesh.position.y = position[1];
			// add the mesh to the scene
			scene.add(mesh);
		}
	});

// create a function to update the scene on every frame
function animate() {
	requestAnimationFrame(animate);
	renderer.render(scene, camera);
}

// start the animation loop
animate();
