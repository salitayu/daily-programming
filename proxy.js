const user = {
    firstName: 'Chris',
    lastName: 'Bongers',
    age: 10,
    address: {
        postalCode: '1234AB'
    }
}

const handler = {
    get(target, key) {
        if (typeof target[key] === 'object' && target[key] !== null) {
            return new Proxy(target[key], handler)
        }
        return target[key]
    },
    set(target, prop, value) {
        console.log(`changed ${prop} from ${target[prop]} to ${value}`)
        target[prop] = value
    }
}

const proxyUser = new Proxy(user, handler)

proxyUser.age = 33
proxyUser.email = 'info@daily-dev-tips.com'
proxyUser.address.postalCode = '5678CD'
