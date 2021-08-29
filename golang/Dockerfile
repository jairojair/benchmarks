FROM golang:1.17-alpine as base

RUN apk update && apk add --no-cache \
	git \
	gcc \
	musl-dev \
	make

FROM base AS echo-builder
WORKDIR /go/src
COPY ./echo/ /go/src
RUN go build -o echo

FROM base AS gin-builder
WORKDIR /go/src
COPY ./gin/ /go/src
RUN go build -o gin

FROM alpine:latest AS echo
COPY --from=echo-builder /go/src/echo .
ENTRYPOINT ["./echo"]
EXPOSE 1323

FROM alpine:latest AS gin
COPY --from=gin-builder /go/src/gin .
ENTRYPOINT ["./gin"]
EXPOSE 8080