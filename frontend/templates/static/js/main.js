const baseUrl = 'https://syne-travel.herokuapp.com/api/v1/'

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


const put = async (url, data, token=null) => {
    let options;

    if (token !== null) {
        options = {
            method: 'PUT',
            body: data,
            headers: new Headers({
                'Accept': '*/*',
                'Authorization': 'JWT ' + token
            })
        }
    }

    delete options.headers['Content-Type'];

    const response = await fetch(url, options);
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

