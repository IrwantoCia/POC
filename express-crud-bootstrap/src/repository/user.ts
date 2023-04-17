import {UserEntity} from "../entity/user";
import {db} from "../database";
import {CreateUserValidator} from "../validation/user/create";

export class UserRepository {
    public static async findOne(id: number): Promise<UserEntity> {
        return db.one('SELECT * FROM "user" WHERE id = $1', id)
    }

    public static async create(user: CreateUserValidator): Promise<UserEntity> {
        return db.one('INSERT INTO "user" (name, email, password) VALUES ($1, $2,$3) RETURNING *', [user.name, user.email, user.password])
    }

    public static async update(id: number, user: CreateUserValidator): Promise<UserEntity> {
        return db.one('UPDATE "user" SET name = $1, email = $2, password = $3 WHERE id = $4 RETURNING *', [user.name, user.email, user.password, id])
    }

    public static async delete(id: number): Promise<UserEntity> {
        return db.one('DELETE FROM "user" WHERE id = $1 RETURNING *', id)
    }
}