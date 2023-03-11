import { PrismaClient } from "@prisma/client";

globalThis.prisma = undefined;

const client = globalThis.prisma || new PrismaClient();
if (process.env.NODE_ENV !== "production") {
    globalThis.prisma = client;
}

module.exports = client;
