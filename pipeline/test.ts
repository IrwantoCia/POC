import {Pipeline} from "./pipeline";

describe('Pipeline', () => {
    it('should run a pipeline', () => {
        expect(true).toBe(true);
    });

    it('should run multiple functions with different types parameter', () => {
        const pipeline = new Pipeline<number>(0);

        const result = pipeline.addFunc((x: number) => x + 1)
            .addFunc((x: number) => x.toString())
            .addFunc((x: string) => x + "2")
            .run();

        expect(result).toBe("12");
    } );
});