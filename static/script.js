document.addEventListener("DOMContentLoaded", function () {


window.onload = function() {
    const primaAlternativa = document.querySelector('#alternative-section .alternativa');
    if (primaAlternativa) {
        const valoriDiv = primaAlternativa.querySelector('.valori_criterii');
        const nrCriterii = document.querySelectorAll('#criterii-section .criteriu').length;
        valoriDiv.innerHTML = '';
        for (let i = 0; i < nrCriterii; i++) {
            valoriDiv.innerHTML += `Valoare criteriu ${i+1}: <input type="number" step="any" name="valoare_criterii[]" required><br>`;
        }
    }
}


window.adaugaCriteriu = function() {
    const div = document.createElement('div');
    div.className = 'criteriu';
    div.innerHTML = `Nume: <input type="text" name="criteriu_nume[]" required>
        Pondere: <input type="number" name="criteriu_pondere[]" step="0.1" required>
        Tip: <select name="criteriu_tip[]">
            <option value="1">MAX</option>
            <option value="0">MIN</option>
        </select>`;
    document.getElementById('criterii-section').appendChild(div);

    const nrCriterii = document.querySelectorAll('#criterii-section .criteriu').length;

    const alternative = document.querySelectorAll('#alternative-section .alternativa');
    alternative.forEach(alt => {
        const valoriDiv = alt.querySelector('.valori_criterii');
        
        const labelNou = document.createElement('label');
        labelNou.textContent = `Valoare criteriu ${nrCriterii}: `;

        const inputNou = document.createElement('input');
        inputNou.type = 'number';
        inputNou.step = 'any';
        inputNou.name = 'valoare_criterii[]';
        inputNou.required = true;

        valoriDiv.appendChild(labelNou);
        valoriDiv.appendChild(inputNou);
        valoriDiv.appendChild(document.createElement('br'));
    });
}


    window.adaugaAlternativa = function() {
                const div = document.createElement('div');
                div.className = 'alternativa';
                div.innerHTML = `Nume: <input type="text" name="alternativa_nume[]" required><br>
                    <div class="valori_criterii"></div>`;
                
                    const valoriDiv = div.querySelector('.valori_criterii');
                const nrCriterii = document.querySelectorAll('#criterii-section .criteriu').length;

                for (let i = 0; i < nrCriterii; i++) {
                    valoriDiv.innerHTML += `Valoare criteriu ${i+1}: <input type="number" step="any" name="valoare_criterii[]" required><br>`;
                }

                document.getElementById('alternative-section').appendChild(div);

            }
});