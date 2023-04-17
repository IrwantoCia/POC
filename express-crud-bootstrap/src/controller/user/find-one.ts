import {NextFunction, Request, Response} from "express";
import {UserRepository} from "../../repository/user";
import {transform} from "../../core/transformer";
import {FindUserTransformer} from "../../transformer/user/find-user";

const findOne = async (req: Request, res: Response, next: NextFunction) => {
    const {id} = req.params;
    try {
        const user = await UserRepository.findOne(+id);
        res.status(200).send({
            status: 200,
            message: 'OK',
            data: transform(FindUserTransformer, user),
        });
    } catch (error) {
        next(error);
    }
}

export default findOne;