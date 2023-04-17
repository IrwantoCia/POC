import {NextFunction, Request, Response} from "express";
import {UserRepository} from "../../repository/user";
import {CreateUserValidator} from "../../validation/user/create";
import {transform} from "../../core/transformer";
import {UpdateUserTransformer} from "../../transformer/user/update";

const update = async (req: Request, res: Response, next: NextFunction) => {
    const validator = new CreateUserValidator({...req.body});
    const {errors, data: payload} = await validator.validate();

    if (errors) {
        return res.status(400).send({
            status: 400,
            message: 'Bad Request',
            data: errors,
        });
    }
    const {id} = req.params;

    try {
        const user = await UserRepository.update(+id, payload);
        res.status(200).send({
            status: 200,
            message: 'OK',
            data: transform(UpdateUserTransformer, user),
        });
    } catch (error) {
        next(error);
    }
}

export default update;