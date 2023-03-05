import NextAuth from 'next-auth'
import AppleProvider from 'next-auth/providers/apple'
import FacebookProvider from 'next-auth/providers/facebook'
import GoogleProvider from 'next-auth/providers/google'
import EmailProvider from 'next-auth/providers/email'

export default NextAuth({
  providers: [
    // OAuth authentication providers...
//    AppleProvider({
//      clientId: process.env.APPLE_ID,
//      clientSecret: process.env.APPLE_SECRET
//    }),
//    FacebookProvider({
//      clientId: process.env.FACEBOOK_ID,
//      clientSecret: process.env.FACEBOOK_SECRET
//    }),
    GoogleProvider({
      clientId: process.env.GOOGLE_ID,
      clientSecret: process.env.GOOGLE_SECRET
    }),
    // Passwordless / email sign in
//    EmailProvider({
//      server: {
//        host: process.env.EMAIL_SERVER_HOST,
//        port: process.env.EMAIL_SERVER_PORT,
//        auth: {
//          user: process.env.EMAIL_SERVER_USER,
//          pass: process.env.EMAIL_SERVER_PASSWORD,
//        },
//      },
//    }),
  ],
  callbacks: {
  async jwt({ token, account }) {
    // Persist the OAuth access_token to the token right after signin
    if (account) {
      token.accessToken = account.access_token
    }
    return token
  },
  async session({ session, token, user }) {
    // Send properties to the client, like an access_token from a provider.
    session.accessToken = token.accessToken
    return session
  }
}
})