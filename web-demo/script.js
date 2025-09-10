const GRID_DIMENSION = 10;
const MIN_TEMP = 150;
const MAX_TEMP = 300;
const MIN_R = 0.0001;
const MAX_R = 1.5;
const MIN_C = 400;
const MAX_C = 500;
const MIN_M = 27;
const MAX_M = 33;
const NUM_OBJECTS = GRID_DIMENSION * GRID_DIMENSION;
const DT = 20;

let T_vector = [];
let R_matrix = [];
let c_vector = []; 
let m_vector = []; 
let isSimulating = false;
let simulationInterval = null;

let T_value = (MAX_TEMP + MIN_TEMP)/2;
let R_value = 0.1;
let c_value = (MAX_C + MIN_C)/2;
let m_value = (MAX_M + MIN_M)/2;

const gridContainer = document.getElementById('grid-container');

const resistanceInput = document.getElementById('resistance-input');
const resistanceValueSpan = document.getElementById('resistance-value');

const heatCapacityInput = document.getElementById('heat-capacity-input');
const heatCapacityValueSpan = document.getElementById('heat-capacity-value');

const massInput = document.getElementById('mass-input');
const massValueSpan = document.getElementById('mass-value');

gridContainer.style.gridTemplateColumns = `repeat(${GRID_DIMENSION}, 1fr)`;

function init() {
    gridContainer.innerHTML = '';
    for (let i = 0; i < NUM_OBJECTS; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.id = `cell-${i}`;
        gridContainer.appendChild(cell);
    }

    R_matrix = [];
    for (let r = 0; r < NUM_OBJECTS; r++) {
        R_matrix[r] = [];
        for (let c = 0; c < NUM_OBJECTS; c++) {
            R_matrix[r][c] = 1000000;
        }
    }

    for (let i = 0; i < NUM_OBJECTS - 1; i++) {
        if((i+1)%GRID_DIMENSION == 0)
            continue;
        else {
            R_matrix[2 + i - 1][1 + i - 1] = R_value;
            R_matrix[1 + i - 1][2 + i - 1] = R_matrix[2 + i - 1][1 + i - 1];
        }
    }

    for (let i = 0; i < NUM_OBJECTS - GRID_DIMENSION; i++) {
        R_matrix[(GRID_DIMENSION+1) + i - 1][1 + i - 1] = R_value;
        R_matrix[1 + i - 1][(GRID_DIMENSION+1) + i - 1] = R_matrix[(GRID_DIMENSION+1) + i - 1][1 + i - 1];
    }

    T_vector = Array.from({ length: NUM_OBJECTS }, () => T_value );
    c_vector = Array.from({ length: NUM_OBJECTS }, () => c_value );
    m_vector = Array.from({ length: NUM_OBJECTS }, () => m_value );

}

function getColor(temperature) {
    const normalizedTemp = (temperature - MIN_TEMP) / (MAX_TEMP - MIN_TEMP);
    const g = Math.floor(255 * (1 - normalizedTemp));
    const b = Math.floor(255 * (1 - normalizedTemp));
    return `rgb(255, ${g}, ${b})`;
}

function updateColors() {
    for (let i = 0; i < T_vector.length; i++) {
        const cell = document.getElementById(`cell-${i}`);
        if (cell) {
            cell.style.backgroundColor = getColor(T_vector[i]);
        }
    }
}

function dot_product(vec1, vec2) {
    result = 0;
    for(let i = 0; i < NUM_OBJECTS; i++) {
        result += vec1[i]*vec2[i];
    }
    return result;
}

// Funzione di simulazione semplificata (NON usa R_matrix e c_vector)
function heat_diffusion_simulation() {
    console.log(T_vector[0]);

    const newT_vector = [...T_vector];

    for (let i = 0; i < NUM_OBJECTS; i++) {

        R_dot = [];
        for (let j = 0; j < NUM_OBJECTS; j++) {
            R_dot[j] = 1 / R_matrix[i][j];
        }

        T_dot = [];
        for (let j = 0; j < NUM_OBJECTS; j++) {
            T_dot[j] = T_vector[i] - T_vector[j];
        }

        delta_T = DT * dot_product(R_dot, T_dot) / (m_vector[i] * c_vector[i]) ;

        console.log(delta_T);

        newT_vector[i] = T_vector[i] - delta_T;
        
    }
    
    T_vector = newT_vector;
}

function toggleSimulation() {
    if (isSimulating) {
        clearInterval(simulationInterval);
        simulateBtn.textContent = 'Avvia Simulazione';
    } else {
        simulationInterval = setInterval(() => {
            heat_diffusion_simulation();
            updateColors();
        }, 25);
        simulateBtn.textContent = 'Ferma Simulazione';
    }
    isSimulating = !isSimulating;
}

resistanceValueSpan.textContent = R_value;
resistanceInput.value = R_value;
resistanceInput.setAttribute('min', MIN_R);
resistanceInput.setAttribute('max', MAX_R);
resistanceInput.addEventListener('input', (event) => {
    R_value = parseFloat(event.target.value);
    resistanceValueSpan.textContent = R_value.toFixed(1);

    for (let i = 0; i < NUM_OBJECTS - 1; i++) {
        if((i+1)%GRID_DIMENSION == 0)
            continue;
        else {
            R_matrix[2 + i - 1][1 + i - 1] = R_value;
            R_matrix[1 + i - 1][2 + i - 1] = R_matrix[2 + i - 1][1 + i - 1];
        }
    }

    for (let i = 0; i < NUM_OBJECTS - GRID_DIMENSION; i++) {
        R_matrix[(GRID_DIMENSION+1) + i - 1][1 + i - 1] = R_value;
        R_matrix[1 + i - 1][(GRID_DIMENSION+1) + i - 1] = R_matrix[(GRID_DIMENSION+1) + i - 1][1 + i - 1];
    }
});

heatCapacityValueSpan.textContent = c_value;
heatCapacityInput.value = c_value;
heatCapacityInput.setAttribute('min', MIN_C);
heatCapacityInput.setAttribute('max', MAX_C);
heatCapacityInput.addEventListener('input', (event) => {
    c_value = parseFloat(event.target.value);
    heatCapacityValueSpan.textContent = c_value.toFixed(1);
    c_vector = Array.from({ length: NUM_OBJECTS }, () => c_value );
});

massInput.value = m_value;
massValueSpan.textContent = m_value;
massInput.setAttribute('min', MIN_M);
massInput.setAttribute('max', MAX_C);
massInput.addEventListener('input', (event) => {
    m_value = parseFloat(event.target.value);
    massValueSpan.textContent = m_value.toFixed(1);
    m_vector = Array.from({ length: NUM_OBJECTS }, () => m_value );
});

init();