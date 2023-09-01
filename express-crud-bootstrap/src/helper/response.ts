import { Response } from "express";

export class HttpResponse {
    public static error(res: Response, errors: string[], status: number): void {
        res.status(status).send({
            errors,
            data: null,
            timestamp: new Date().getTime()
        });
    }

    public static success(res: Response, data: unknown, status: number): void {
        res.status(status).send({
            errors: [],
            data: data,
            timestamp: new Date().getTime()
        });
    }
};
