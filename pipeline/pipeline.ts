type Func<T, U> = (arg: T) => U | Promise<U>;
type Fn = {
    fn: Func<any, any>;
    param: any;
}

export class Pipeline<T> {
    private readonly initialValue: T;
    private fnList: Fn[] = [];

    constructor(init: T) {
        this.initialValue = init;
    }

    addFunc<U>(func: Func<T | unknown, U>, overrideParam?: unknown) {
        this.fnList.push({fn: func, param: overrideParam});
        return this as unknown as Pipeline<U | unknown>;
    }

    async run() {
        let result = this.initialValue;
        for (const func of this.fnList) {
            if (func.param) {
                result = await func.fn(func.param);
                continue;
            }
            result = func.fn(result);
        }
        return result;
    };
}

type User = {
        name: string;
        age: number;
    }

type UserDto = {
    name: string;
}

function findUserById(id: number): Promise<User> {
    return Promise.resolve({name: 'John', age: 20});
}

function createUser(user: UserDto):User {
    return {
        name: user.name,
        age: 20,
    };
}

function isUserExist(user: User) {
    return
}

const userDto: UserDto = {
    name: 'John',
}

function test() {
    const pipeline = new Pipeline<number>(1);
    return pipeline
        .addFunc(findUserById)
        .addFunc(isUserExist)
        .addFunc(createUser, userDto)
        .run();
}

test().then(value => console.log(value));