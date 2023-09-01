import { z, ZodError } from "zod";

const _CreateUser = z.object({
    name: z.string(),
    email: z.string().email(),
    password: z.string().min(6),
});

type Result = {
    data: z.infer<typeof _CreateUser> | null,
    error: ZodError | null,
}

type ResultSuccess = {
    data: z.infer<typeof _CreateUser>,
    error: null,
}

type ResultError = {
    data: null,
    error: ZodError,
}

class UserValidator {
    public static createUser(data: any) {
        const result = _CreateUser.safeParse(data);
        if (!result.success) {
            return {
                data: null,
                error: result.error,
            } as ResultError
        } else {
            return {
                data: result.data,
                error: null,
            } as ResultSuccess
        }
    }
}

export default UserValidator;
