import {Router} from 'express';
import findOne from "../controller/user/find-one";
import create from "../controller/user/create";
import update from "../controller/user/update";
import destroy from "../controller/user/destroy";

const router = Router();
router.get('/:id', findOne);
router.post('/', create);
router.put('/:id', update);
router.delete('/:id', destroy);

export default router;