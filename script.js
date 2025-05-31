function showScreen(screen) {
  document.getElementById('surveyScreen').style.display = screen === 'survey' ? 'block' : 'none';
  document.getElementById('resultsScreen').style.display = screen === 'results' ? 'block' : 'none';
  if (screen === 'results') showResults();
}

function calculateAge(dob) {
  const birthDate = new Date(dob);
  const today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  const m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
  return age;
}

function submitSurvey() {
  const fullname = document.getElementById('fullname').value.trim();
  const email = document.getElementById('email').value.trim();
  const contact = document.getElementById('contact').value.trim();
  const dob = document.getElementById('birthDate').value;

  if (!fullname || !email || !contact || !dob) {
    alert('Please complete all personal details.');
    return;
  }

  const age = calculateAge(dob);
  if (age < 5 || age > 120) {
    alert('Age must be between 5 and 120 based on your date of birth.');
    return;
  }

  const food = Array.from(document.querySelectorAll('input[type=checkbox]:checked')).map(cb => cb.value);
  if (food.length === 0) {
    alert('Please select at least one favourite food.');
    return;
  }

  const ratings = {};
  for (let category of ['eatout', 'movies', 'tv', 'radio']) {
    const selected = document.querySelector(`input[name=${category}]:checked`);
    if (!selected) {
      alert(`Please rate: ${category}`);
      return;
    }
    ratings[category] = parseInt(selected.value);
  }

  const payload = {
    fullname,
    email,
    contact,
    date: dob,
    age,
    food,
    ...ratings
  };

  fetch('http://127.0.0.1:5000/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message || 'Submitted!');
    location.reload();
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Failed to submit. Is the server running?');
  });
}

function showResults() {
  fetch('http://127.0.0.1:5000/results')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('resultsContent');
      if (!data || data.total === 0 || data.message === 'No Surveys Available') {
        container.innerHTML = '<p>No Surveys Available</p>';
        return;
      }

      container.innerHTML = `
        <table>
          <tr><th>Total Surveys</th><td>${data.total}</td></tr>
          <tr><th>Average Age</th><td>${data.avg_age}</td></tr>
          <tr><th>Oldest Participant</th><td>${data.oldest}</td></tr>
          <tr><th>Youngest Participant</th><td>${data.youngest}</td></tr>
          <tr><th>% Who Like Pizza</th><td>${data.pizza_percent}%</td></tr>
          <tr><th>Avg. 'Eat Out' Rating</th><td>${data.eatout_avg}</td></tr>
        </table>`;
    })
    .catch(error => {
      console.error('Error fetching results:', error);
      document.getElementById('resultsContent').innerHTML = '<p>Error fetching results.</p>';
    });
}

showScreen('survey');
