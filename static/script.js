document.addEventListener("DOMContentLoaded", function () {

    window.adaugaCriteriu = function() {
                const div = document.createElement('div');
                div.className = 'criteriu';
                div.innerHTML = `Nume: <input type="text" name="criteriu_nume[]" required>
                    Pondere: <input type="number" name="criteriu_pondere[]" step="0.01" required>
                    Tip: <select name="criteriu_tip[]">
                        <option value="1">Beneficiu</option>
                        <option value="0">Cost</option>
                    </select>`;
                document.getElementById('criterii-section').appendChild(div);
                actualizeazaValoriCriterii();
            }

    window.adaugaAlternativa = function() {
                const div = document.createElement('div');
                div.className = 'alternativa';
                div.innerHTML = `Nume: <input type="text" name="alternativa_nume[]" required><br>
                    <div class="valori_criterii"></div>`;
                document.getElementById('alternative-section').appendChild(div);
                actualizeazaValoriCriterii();
            }

            function actualizeazaValoriCriterii() {
                const nrCriterii = document.querySelectorAll('#criterii-section .criteriu').length;
                const alternative = document.querySelectorAll('#alternative-section .alternativa');
                alternative.forEach(alt => {
                    const valoriDiv = alt.querySelector('.valori_criterii');
                    valoriDiv.innerHTML = '';
                    for (let i = 0; i < nrCriterii; i++) {
                        valoriDiv.innerHTML += `Valoare criteriu ${i+1}: <input type="number" step="any" name="valoare_criterii[]" required><br>`;
                    }
                });
            }

            actualizeazaValoriCriterii();
});