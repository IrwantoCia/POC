import {NextFunction, Request, Response} from "express";
import {UserRepository} from "../../repository/user";
import {transform} from "../../core/transformer";
import {DestroyUserTransformer} from "../../transformer/user/destroy";

const destroy = async (req: Request, res: Response, next: NextFunction) => {
    const {id} = req.params;
    try {
        const user = await UserRepository.delete(+id);
        res.status(200).send({
            status: 200,
            message: 'OK',
            data: transform(DestroyUserTransformer, user),
        })
    } catch (error) {
        next(error);
    }
}

export default destroy;

