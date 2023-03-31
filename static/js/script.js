let text = document.getElementById('text');
let cloud_1 = document.getElementById('cloud_1');
let cloud_2 = document.getElementById('cloud_2');
let cloud_3 = document.getElementById('cloud_3');
let cloud_4 = document.getElementById('cloud_4');
let cloud_5 = document.getElementById('cloud_5');
let cloud_6 = document.getElementById('cloud_6');
// let island_center = document.getElementById('island_center');
let island_left = document.getElementById('island_left');
let island_right = document.getElementById('island_right');
let fog = document.getElementById('fog');

window.addEventListener('scroll',() =>{
	let value = window.scrollY;

	text.style.marginTop = value * 2.5 + 'px';
    cloud_1.style.left = value * 1.5 + 'px';
    cloud_2.style.left = value * -1.5 + 'px';
    cloud_3.style.left = value * -1.5 + 'px';
    cloud_4.style.left = value * 1.5 + 'px';
    cloud_5.style.left = value * -1.5 + 'px';
    cloud_6.style.left = value * -1.5 + 'px';
    // island_center.style.left = value * -1.5 + 'px';
    island_left.style.left = value * -1.5 + 'px';
    island_right.style.left = value * 1.5 + 'px';
})