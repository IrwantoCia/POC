import {ClassTransformOptions, plainToInstance} from "class-transformer";

const transformerOptions: ClassTransformOptions = {
    excludeExtraneousValues: true,
};

export function transform<T>(classType: new () => T, item: unknown): T {
    return plainToInstance(classType, item, transformerOptions);
}

export function transformCollection<T>(
    classType: new () => T,
    items: unknown[],
): T[] {
    return items.map((item) => transform(classType, item));
}
