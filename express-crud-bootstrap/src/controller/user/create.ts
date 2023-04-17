import {NextFunction, Request, Response} from "express";
import {UserRepository} from "../../repository/user";
import {CreateUserValidator} from "../../validation/user/create";
import {transform} from "../../core/transformer";
import {CreateUserTransformer} from "../../transformer/user/create";

const create = async (req: Request, res: Response, next: NextFunction) => {
    const validator = new CreateUserValidator({...req.body});
    const {errors, data: payload} = await validator.validate();

    if (errors) {
        return res.status(400).send({
            status: 400,
            message: 'Bad Request',
            data: errors,
        });
    }

    try {
        const user = await UserRepository.create(payload);
        res.status(201).send({
            status: 201,
            message: 'OK',
            data: transform(CreateUserTransformer, user),
        });
    } catch (error) {
        next(error);
    }
}

export default create;
