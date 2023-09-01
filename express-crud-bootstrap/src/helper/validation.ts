import { ZodError, ZodIssue } from 'zod';

//result.error.issues;
/* [
    {
      "code": "invalid_type",
      "expected": "string",
      "received": "number",
      "path": [ "name" ],
      "message": "Expected string, received number"
    }
] */

/*
    * {
    *   email: "invalid email",
    *   password: "invalid password"
    *   name: "required"
    * }
    * */
export const getErrorMessages = (error: ZodError): { data: string[], error: Error | null } => {
    try {
        return {
            data: error.issues.map((issue: ZodIssue) => (`${issue.path[0]}: ${issue.message.toLowerCase()}`)),
            error: null
        }

    } catch (error: unknown) {
        return {
            data: [],
            error: error as Error
        }
    }
}

