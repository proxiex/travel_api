const baseUrl = 'https://syne-travel.herokuapp.com/api/v1/'

const post = (url, data) => fetch(url, {
    credentials: 'same-origin',
    method: 'POST',
    body: JSON.stringify(data),
    headers: new Headers({
        'Content-Type': 'application/json'
    }),
}).then(response => response.json())

const get = (url, data) => fetch(url, {
    credentials: 'same-origin',
    method: 'GET',
    headers: new Headers({
        'Content-Type': 'application/json'
    }),
}).then(response => response.json())

const elmById = (id) => {
    return document.getElementById(id)
}

const isLogedIn = () => {
    token = window.localStorage.getItem('userToken')
    if(token) {
        return token;
    } else {
        return false;
    }
}

const logout = () => {
    window.localStorage.removeItem('userToken')
    window.location = '../'
}

