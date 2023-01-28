# How to Run the Torchlite App
The Torchlite App has two parts:

1. A front-end application (a NextJS web app)
2. A back-end application (a Python FastAPI application)

At this point in development, either of these applications may be run separately; the front end does not need the back end to run, nor does the back end need the front end to run. (This will change.)

## Running the back end (Flask app)
The back-end Flask application resides in the api/ directory. To run the back-end Flask application, you need to activate its Python virtual environment and start the application.
```
cd api
poetry run uvicorn ./src/api/main:tlapi --reload
```

## Running the front end (NextJS app)
To start the front-end application, start another interactive shell, move to the top-level directory and run 

```
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.tsx`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.ts`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
