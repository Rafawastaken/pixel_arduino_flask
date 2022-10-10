const boxes = document.querySelectorAll(".cel");
let estado_enviar = "0";

boxes.forEach((box) => {
  box.addEventListener("click", function handleClick(event) {
    // ID Pixel carregado
    var pixel_id = box.getAttribute("id");

    estado_enviar = change_color(box);
    send_position(pixel_id, estado_enviar);
  });
});

function change_color(box) {
  const current_color = box.getAttribute("class").split(" ")[1];
  if (current_color === "blank") {
    box.classList.remove("blank");
    box.classList.add("colored");
    estado_enviar = "1";
  }
  if (current_color === "colored") {
    box.classList.remove("colored");
    box.classList.add("blank");
    estado_enviar = "0";
  }

  return estado_enviar;
}

function send_position(pixel_id, estado_enviar) {
  let xhr = new XMLHttpRequest();

  xhr.open("POST", "http://127.0.0.1:5000/post-matrix/" + pixel_id);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(
    JSON.stringify({
      estado: estado_enviar,
    })
  );
}
