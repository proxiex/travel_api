const baseUrl = 'http://127.0.0.1:8000/api/v1/'

const post = async (url, data, token=null) => {
    let headers;

    if (token !== null) {
        headers = new Headers({
            'Content-Type': 'application/json',
            'Authorization': 'JWT ' + token
        });
    } else {
        headers = new Headers({
            'Content-Type': 'application/json',
        });
    }

    console.log('00000000', headers)

    const response = await fetch(url, {
        credentials: 'same-origin',
        method: 'POST',
        body: JSON.stringify(data),
        headers,
    });
    return await response.json();
}

const get = async (url, token = null) => {
    let headers;

    if (token !== null) {
        headers = new Headers({
            'Content-Type': 'application/json',
            'Authorization': 'JWT ' + token
        });
    } else {
        headers = new Headers({
            'Content-Type': 'application/json',
        });
    }

    const response = await fetch(url, {
        credentials: 'same-origin',
        method: 'GET',
        headers,
    });
    return await response.json();
}

const elmById = (id) => {
    return document.getElementById(id)
}

const isLogedIn = () => {
    const token = window.localStorage.getItem('userToken')
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

