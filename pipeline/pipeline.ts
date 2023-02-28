type Func<T, U> = (arg: T) => U | Promise<U>;

export class Pipeline<T> {
    private readonly initialValue: T;
    private fn: Func<any, any>[] = [];

    constructor(init: T) {
        this.initialValue = init;
    }

    addFunc<U>(func: Func<T, U>): Pipeline<U> {
        this.fn.push(func);
        return this as unknown as Pipeline<U>;
    }

    async run() {
        let result = this.initialValue;
        for (const func of this.fn) {
            result = func(result);
            if (result instanceof Promise) {
                result = await result;
            }
        }
        return result;
    }
}
