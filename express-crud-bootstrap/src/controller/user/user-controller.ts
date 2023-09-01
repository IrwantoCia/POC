import { NextFunction, Response, Request } from "express";

import { getErrorMessages } from "../../helper/validation";
import { HttpResponse } from "../../helper/response";
import { UserRepository } from "../../repository/user";
import UserValidator from "../../validation/user";

class UserController {
    public static async get(req: Request, res: Response, next: NextFunction) {
        // ...
    }

    public static async delete(req: Request, res: Response, next: NextFunction) {
        // ...
    }

    public static async update(req: Request, res: Response, next: NextFunction) {
        // ...
    }

    public static async create(req: Request, res: Response, next: NextFunction) {
        const validation = UserValidator.createUser(req.body);

        if (validation.error) {
            const errorMessages = getErrorMessages(validation.error);
            errorMessages.error && next(errorMessages.error);
            HttpResponse.error(res, errorMessages.data, 400);
        } else {
            if (UserService.isUserExist(validation.data.email)) {
                HttpResponse.error(res, ["user already exists"], 400);
            }

            const user = await UserRepository.create(validation.data);
            user.error && next(user.error);

            HttpResponse.success(res, user.data, 201);
        }

    }
}

export default UserController;

class UserService {
    public static isUserExist(email: string): boolean {
        return true;
        // ...
    }
}
