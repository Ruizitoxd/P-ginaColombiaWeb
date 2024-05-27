const botonImportJson = document.querySelector("#jsonImport");
const selectFlores = document.querySelector("#flores");
const descFlores = document.querySelector("#DescFlores");
const textoEspe = document.querySelector("#TextoEspe");
const textoTotal = document.querySelector("#TextoTotal");

const data = async()=>{
    try {
        const response = await fetch("./Exportacion.json");
        const datos = await response.json();

        return datos;
    } catch (error) {
        return error;
    }
}

const fillSelect = (jsonData)=>{
    selectFlores.innerHTML = `<option value="">Seleccione su flor</option>`;

    const {especies, ...flores} = jsonData;

    const arrayFlores = Object.values(flores);

    arrayFlores.forEach((flor)=>{
        selectFlores.innerHTML += `
            <option value="${flor.Nombre}">${flor.Nombre}</option>
        `
    })

    textoEspe.innerHTML = `${especies.Total} especies<br>en Colombia`
    textoTotal.innerHTML = `${especies.CantidadTotal} ocurrencias de<br>especies estimadas<br>en Colombia`
}

const fillFLorInfo = async (value)=>{
    const jsonData = await data();
    
    const flor = jsonData[value];
    
    descFlores.innerHTML = `
        <div class="TextoBloq"><p class="florInfo">Nombre: </p><p class="florDato">${flor.Nombre}</p></div>
        <div class="TextoBloq"><p class="florInfo">Nombre Cientifico: </p><p class="florDato">${flor.NombreCientifico}</p></div>
        <div class="TextoBloq"><p class="florInfo">Reino: </p><p class="florDato">${flor.Reino}</p></div>
        <div class="TextoBloq"><p class="florInfo">Phylum: </p><p class="florDato">${flor.Phylum}</p></div>
        <div class="TextoBloq"><p class="florInfo">Clase: </p><p class="florDato">${flor.Clase}</p></div>
        <div class="TextoBloq"><p class="florInfo">Orden: </p><p class="florDato">${flor.Orden}</p></div>
        <div class="TextoBloq"><p class="florInfo">Familia: </p><p class="florDato">${flor.Familia}</p></div>
        <div class="TextoBloq"><p class="florInfo">Genero: </p><p class="florDato">${flor.Genero}</p></div>
        <div class="TextoBloq"><p class="florInfo">Especie: </p><p class="florDato">${flor.Especie}</p></div>
        <div class="TextoBloq"><p class="florInfo">Ubicacion: </p><p class="florDato">${flor.Departamento}, extendiendose por el Conglomerado #${flor.Conglomerado}</p></div>
        <div class="TextoBloq"><p class="florInfo">Brigada: </p><p class="florDato">Descubierto por la brigada #${flor.Brigada}</p></div>
        `
    const departamentoso = document.querySelector(`#${flor.IdDepartamento}`);
    departamentoso.style = "fill: #4cc9c9";
    const oldDepartamento = localStorage.getItem("departamento");
    if (oldDepartamento == null){
        localStorage.setItem("departamento", flor.IdDepartamento);
    } else if (departamentoso.id == oldDepartamento){
        departamentoso.style = "fill: #4cc9c9";
    } 
    else {
        const VariableX = document.querySelector(`#${localStorage.getItem("departamento")}`);
        VariableX.style = "fill: #95cbcf";
        localStorage.setItem("departamento", flor.IdDepartamento);
    }
}

ImportarBT.addEventListener('click', async (e)=>{
    e.preventDefault();
    
    const datos = await data();

    fillSelect(datos);    
})

selectFlores.addEventListener('change', (e)=>{
    e.preventDefault();

    const value = e.target.value;

    fillFLorInfo(value)
})