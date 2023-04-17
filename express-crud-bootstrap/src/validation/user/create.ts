import {IsString, validate} from "class-validator";

export class CreateUserValidator {
    @IsString()
    name: string;

    @IsString()
    email: string;

    @IsString()
    password: string;

    constructor({name, email, password}: { name: string, email: string, password: string }) {
        this.name = name;
        this.email = email;
        this.password = password;
    }

    public async validate() {
        const errors = await validate(this);
        if (errors.length) {
            return {
                data: this,
                errors: errors,
            };
        }

        return {
            data: this,
            errors: null,
        };
    }
}