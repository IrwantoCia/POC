import {UserEntity} from "../../entity/user";
import {Expose} from "class-transformer";

export class FindUserTransformer implements Omit<UserEntity, "password"> {
    @Expose() id: number = 0
    @Expose() email: string = "";
    @Expose() name: string = "";
}