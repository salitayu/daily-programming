const employees = [{
    'id': 1,
    'fulltime': 'yes',
    'reports': [
        {
            'id': 2,
            'name': true,
            'fulltime': true,
            'playsvideogames': false,
            'reports': [{
                'id': 3,
                'name': 1,
                'fulltime': true,
                'reports': [{
                    'id': 4,
                    'name': 'hello',
                    'fulltime': 'hi',
                    'plays': true,
                    'reports': [{
                        'id': 8,
                        'name': 'hello',
                        'fulltime': 'hi',
                        'plays': true,
                        'reports': [{
                            'id': 9,
                            'name': true,
                            'fulltime': 'hey',
                            'plays': true
                        }]
                    }]
                }]
            }]
        },
        {
            'id': 3,
            'name': 'drake',
            'fulltime': true,
            'sings': true
        }
    ]
}]

const schema = {
    'employee': [
        {
            'name': 'id',
            'required': true,
            'type': 'number'
        },
        {
            'name': 'name',
            'required': true,
            'type': 'string'
        },
        {
            'name': 'reports',
            'required': false,
            'type': 'array:employee'
        }
    ]
}

let times = 0
let errors = []
let schemaKeys = []
const validateObjectWithSchema = (employees, schema) => {
    for (let i = 0; i < employees.length; i++) {
        const currentEmployee = employees[i]
        console.log('currentEmployee ', currentEmployee)
        console.log('schema ', schema)
        for (let j = 0; j < schema.employee.length; j++) {
            const currentSchema = schema.employee[j]
            const name = currentSchema.name
            const type = currentSchema.type
            const required = currentSchema.required
            schemaKeys.push(name)

            if (type !== 'array:employee') {
                console.log('name ', currentEmployee[name])
                console.log('type ', typeof currentEmployee[name])
                if (!(name in currentEmployee) && required) {
                    errors.push({message: `${name} is required`})
                } else if (typeof currentEmployee[name] !== type) {
                    const currentType = typeof currentEmployee[name]
                    errors.push({ message: `${name} is of type ${currentType} and not of type ${type}`})
                } else {
                    continue
                }
            } else {
                if (!('reports' in currentEmployee)) {
                    break
                }
                times += 1
                if (times === 3) {
                    break
                }
                validateObjectWithSchema(currentEmployee.reports, schema)
            }
        }
    }
    validateKeys(employees, schemaKeys, errors)
    if (errors.length === 0) {
        errors.push({ message: 'ok' })
    }
    return errors
}

const validateKeys = (employees, schemaKeys, errors) => {
    let hasReports = []
    for (let i = 0; i < employees.length; i++) {
        const employeeKeys = Object.keys(employees[i])
        if (employeeKeys.includes('reports')) {
            hasReports.push(i)
        }
        for (let j = 0; j < employeeKeys.length; j++) {
            if (!schemaKeys.includes(employeeKeys[j])) {
                errors.push({ message: `${employeeKeys[j]} is not in schema`})
            }
        }
    }
    for (let i of hasReports) {
        validateKeys(employees[i].reports, schemaKeys, errors)
    }
    return errors
}

console.log(validateObjectWithSchema(employees, schema))
